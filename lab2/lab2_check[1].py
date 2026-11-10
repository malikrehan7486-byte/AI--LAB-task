"""Run and print the reproducible seven-percept stateful transition trace."""
import json
from pathlib import Path
from lab2_model import ClassroomAgent

ROOT = Path(__file__).resolve().parent
percepts = json.loads((ROOT / "inputs" / "classroom_percepts.json").read_text(encoding="utf-8-sig"))["percepts"]
agent = ClassroomAgent()
print("step | previous mode | percept | target mode | command outcome")
for step, percept in enumerate(percepts, 1):
    previous, target, send = agent.act(percept["temperature_c"], percept["occupied"])
    print(f"{step} | {previous if previous is not None else 'None'} | ({percept['temperature_c']} C, occupied={percept['occupied']}) | {target} | {'SEND' if send else 'NO COMMAND'}")
