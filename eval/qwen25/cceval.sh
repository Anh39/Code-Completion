export LC_ALL="POSIX"

INPUT_MODEL=Qwen/Qwen2.5-Coder-0.5B-Instruct
OUTPUT_DIR=/kaggle/working
TP=2

export TOKENIZERS_PARALLELISM=false
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1

echo "Running CrossCodeEval"
mkdir -p ${OUTPUT_DIR}/cceval
python /kaggle/input/qwen25-benchmark-code/cceval.py     --task line_completion     --model_type codelm_right_cfc_left     --model_name_or_path ${INPUT_MODEL}     --cfc_seq_length 2048     --right_context_length 2048     --prompt_file /kaggle/input/fim-evaluate-data/cceval/LANGUAGE/line_completion_oracle_bm25.jsonl     --gen_length 50     --max_seq_length 8192     --max_model_length 8256     --output_dir ${OUTPUT_DIR}     --dataset cceval     --tp ${TP}     --ts_lib /kaggle/input/tree-sitter-language/LANGUAGE-lang-parser.so     --language python
