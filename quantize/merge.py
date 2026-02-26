import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

def merge(base_model_name: str, lora_path: str, output_path: str, dtype: torch.dtype = torch.bfloat16):
    check_prompt = "<|fim_prefix|><|endoftext|>"
    base_tokenizer = AutoTokenizer.from_pretrained(base_model_name)
    old_ids = base_tokenizer(check_prompt)["input_ids"]
    base_model = AutoModelForCausalLM.from_pretrained(base_model_name, dtype=dtype, device_map="cpu")
    model = PeftModel.from_pretrained(base_model, lora_path)
    model = model.merge_and_unload() #type:ignore
    base_tokenizer.save_pretrained(output_path)
    model.save_pretrained(output_path)
    peft_tokenizer = AutoTokenizer.from_pretrained(output_path)
    peft_ids = peft_tokenizer(check_prompt)["input_ids"]
    assert len(old_ids) == len(peft_ids) and [old_ids[i] == peft_ids[i] for i in range(len(old_ids))]
    print("Model merged completed, saved to", output_path)

