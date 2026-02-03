#!/bin/bash
# Titanium Global Cloud Bridge [cite: 2026-02-02]

# 1. API Szerver beállítása
export KUBECONFIG=GLOBAL_API_SERVER_KUBECONFIG

# 2. Projekt létrehozása (automatikus ID generálással)
PROJECT_ID="titanium-enterprise-$(date +%s)"

echo "🏗️ Projekt létrehozása: $PROJECT_ID..."
kubectl --kubeconfig=${KUBECONFIG} apply -f - <<EOF
apiVersion: resourcemanager.global.gdc.goog/v1
kind: Project
metadata:
  namespace: platform
  name: $PROJECT_ID
