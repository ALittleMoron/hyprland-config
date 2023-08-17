#!/usr/bin/env bash

. ~/.config/hypr/utils.conf

CPU_TEMP="Path to sensor not found"
GPU_TEMP="Path to sensor not found"
NVME_TEMP="Path to sensor not found"

CPU_PATH="/sys/class/hwmon/hwmon$HWMON_CPU_NUM/temp1_input"
GPU_PATH="/sys/class/hwmon/hwmon$HWMON_GPU_NUM/temp1_input"
NVME_PATH="/sys/class/hwmon/hwmon$HWMON_NVME_NUM/temp1_input"

if [[ -f "$CPU_PATH" ]]; then
  CPU_TEMP=$((`cat $CPU_PATH`/1000))°C
fi

if [[ -f "$GPU_PATH" ]]; then
  GPU_TEMP=$((`cat $GPU_PATH`/1000))°C
fi

if [[ -f "$NVME_PATH" ]]; then
  NVME_TEMP=$((`cat $NVME_PATH`/1000))°C
fi

printf "System temperatures:\nCPU: $CPU_TEMP\nGPU: $GPU_TEMP\nNVME: $NVME_TEMP"
