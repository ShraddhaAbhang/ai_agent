from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import pipeline
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Load a summarization model using HuggingFace's pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# LangChain wrapper for the summarizer
class CustomLLM:
    def __call__(self, prompt: str) -> str:
        summary = summarizer(prompt, max_length=50, min_length=25, do_sample=False)
        return summary[0]["summary_text"]

# Setup LangChain
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}",
)
llm = CustomLLM()
chain = LLMChain(llm=llm, prompt=prompt)

# Define request body for JSON API
class SummarizationRequest(BaseModel):
    text: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Summarization App</title>
    </head>
    <body>
        <h1>Summarization App</h1>
        <form id="summarizationForm">
            <textarea name="text" id="text" rows="10" cols="50" placeholder="Enter text to summarize"></textarea><br>
            <button type="submit">Summarize</button>
        </form>
        <h2>Summary</h2>
        <p id="summary"></p>

        <script>
            document.getElementById("summarizationForm").addEventListener("submit", async (e) => {
                e.preventDefault();
                const text = document.getElementById("text").value;
                const response = await fetch("/summarize", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ text }),
                });
                const data = await response.json();
                document.getElementById("summary").textContent = data.summary || "Error summarizing text.";
            });
        </script>
    </body>
    </html>
    """

@app.post("/summarize", response_class=JSONResponse)
async def summarize(request: SummarizationRequest):
    input_text = request.text
    if not input_text:
        return JSONResponse(content={"error": "No text provided"}, status_code=400)
    summary = chain.run(text=input_text)
    return {"summary": summary}

if __name__ == "__main__":
    # Run the app using uvicorn
    uvicorn.run("summarize:app", host="0.0.0.0", port=8090, reload=True)