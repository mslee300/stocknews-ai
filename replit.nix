{ pkgs }: {
  deps = [
    pkgs.mailutils
    pkgs.nodePackages.vscode-langservers-extracted
    pkgs.nodePackages.typescript-language-server
  ];
}