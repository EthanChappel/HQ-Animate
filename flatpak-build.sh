#!/bin/bash

set -e

TMP_DIR=$(mktemp -d -t hqa-flatpak-build-XXXXXXXXXX)

function cleanup {
  rm -rf "$TMP_DIR"
}

trap cleanup EXIT

flatpak-builder --repo $TMP_DIR/flatpak-repo --force-clean --install-deps-from flathub $TMP_DIR/flatpak-build-dir --state-dir $TMP_DIR/flatpak-builder ./com.chappelastro.HQAnimate.json
flatpak build-bundle $TMP_DIR/flatpak-repo ./HQAnimate.flatpak com.chappelastro.HQAnimate