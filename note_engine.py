from llama_index.core.tools import FunctionTool
import os

note_file = os.path.join("datasets", "notes.txt")

def save_notes(note):
    if not os.path.exists(note_file):
        open(note_file, "w")

    with open(note_file, "a") as file:
        file.write(note + "\n")

    return "Note saved successfully."

note_engine = FunctionTool.from_defaults(
    fn=save_notes,
    name='note_engine',
    description='Save notes to a text file.',
)