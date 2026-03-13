#!/usr/bin/env bash
# Start one or more RMBG (background removal) HTTP service processes.
# Usage: ./run_rmbg_servers.sh [N]   (default N=1)
# Ports: 9101, 9102, ... (one per process).

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="${CONFIG:-$PROJECT_ROOT/config/config.yaml}"
N="${1:-1}"

if [[ ! -f "$CONFIG" ]]; then
  echo "Config not found: $CONFIG (copy config/config.yaml.example to config/config.yaml)"
  exit 1
fi

for ((i=0; i<N; i++)); do
  PORT=$((9101 + i))
  echo "Starting RMBG service on port $PORT ..."
  python -m sam3_service.rmbg_server \
    --config "$CONFIG" \
    --port "$PORT" &
done
wait
