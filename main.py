import typer
from pathlib import Path
from litellm import completion

app = typer.Typer()

@app.command()
def main(file_path: str):
    system_prompt = Path("system_prompt.md").read_text()
    user_prompt = Path(file_path).read_text()
    response = completion(
        model="openai/gpt-4o",
        messages=[
            { "content": system_prompt,"role": "system"},
            { "content": user_prompt,"role": "user"}
        ]
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    app()
