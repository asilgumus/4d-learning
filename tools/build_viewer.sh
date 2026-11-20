#!/bin/sh
# Kullanım: sh tools/build_viewer.sh   (Node gerekir; three.js geçici klasöre kurulur)
set -e
R=$(cd "$(dirname "$0")/.." && pwd); T=$(mktemp -d)
cd "$T" && npm init -y >/dev/null && npm i --silent three@0.160.1 esbuild@0.21.5
cp "$R/tools/viewer.src.js" "$T/viewer.src.js"
npx esbuild viewer.src.js --bundle --minify --format=iife --target=es2019 --outfile="$R/site/assets/viewer.js"
