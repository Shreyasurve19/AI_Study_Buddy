import gradio as gr
from google import genai
 
def study_buddy(api_key, language, option, user_input):

    if not api_key:
        return "Please enter your API key."
    if not user_input:
        return "Please enter topic or notes."

    client = genai.Client(api_key=api_key)
 
    # Language instruction
    lang_instruction = f"Respond in {language}."
 
    if option == "Explain Topic":
        prompt = f"{lang_instruction} Explain {user_input} in simple words using bullet points and one example."
    elif option == "Summarize Notes":
        prompt = f"{lang_instruction} Summarize this in simple words using 5 bullet points:\n{user_input}"
    elif option == "Generate Quiz":
        prompt = f"{lang_instruction} Create 5 MCQs with answers about {user_input} in simple language."
    elif option == "Create Flashcards":
        prompt = f"{lang_instruction} Create 5 flashcards (Q and A format) about {user_input}."
 
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
 
 
#Interface
app = gr.Interface(
    fn=study_buddy,
    inputs=[
        gr.Textbox(label="Enter Gemini API Key", type="password"),
        gr.Dropdown(
            ["English", "Marathi", "Hindi", "Spanish", "French"],
            label="Choose Language"
        ),
        gr.Dropdown(
            ["Explain Topic", "Summarize Notes", "Generate Quiz", "Create Flashcards"],
            label="Choose Feature"
        ),
        gr.Textbox(label="Enter Topic or Notes", lines=6)
    ],
    outputs=gr.Textbox(label="Result"),
    title="<h1><b>📚 AI Study Buddy</b></h1>",
    description="<h3><b>Your Smart Learning Assistant with Multilingual Support!</b></h3>"
)
app.launch() 