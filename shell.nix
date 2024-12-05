{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python312
    python312Packages.sly
    python312Packages.autopep8
    python312Packages.pip
    python312Packages.build
    zip
  ];
}
