#!/bin/sh
set -e
flatpak-builder --repo ./flatpak-repo --force-clean --install-deps-from flathub ./flatpak-build-dir com.chappelastro.HQAnimate.json
flatpak build-bundle ./flatpak-repo HQAnimate.flatpak com.chappelastro.HQAnimate
