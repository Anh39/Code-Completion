
export LC_ALL="POSIX"

INPUT_MODEL=Qwen/Qwen2.5-Coder-0.5B-Instruct
OUTPUT_DIR=/kaggle/working/humaneval-infilling
TP=2


mkdir -p ${OUTPUT_DIR}/humaneval-infilling
python /kaggle/input/qwen25-benchmark-code/humaneval-fim.py     --model_type codelm_leftright_context     --model_name_or_path ${INPUT_MODEL}     --input_file /kaggle/input/fim-evaluate-data/humaneval/fim_singleline.jsonl     --max_model_length 8256     --output_dir ${OUTPUT_DIR}     --tp ${TP}
