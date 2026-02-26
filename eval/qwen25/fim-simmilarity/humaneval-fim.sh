export LC_ALL="POSIX"
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export CUDA_VISIBLE_DEVICES=0

INPUT_MODEL=/home/jovyan/anh-uet/models/merged/qwen25-15-test
OUTPUT_DIR=output
TP=1


mkdir -p ${OUTPUT_DIR}/humaneval-infilling
python humaneval-fim.py \
    --model_type codelm_leftright_context \
    --model_name_or_path ${INPUT_MODEL} \
    --input_file data/humaneval/fim_singleline.jsonl \
    --max_model_length 8256 \
    --output_dir ${OUTPUT_DIR} \
    --tp ${TP} \
    --vram_utilization 0.1
