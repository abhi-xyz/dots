{ config, pkgs, ... }:
{
	programs.neovim = 
		let
		toLua = str: "lua << EOF\n${str}\nEOF\n";
	toLuaFile = file: "lua << EOF\n${builtins.readFile file}\nEOF\n";
	in
	{
		enable = true;
		viAlias = true;
		vimAlias = true;
		vimdiffAlias = true;

plugins = with pkgs.vimPlugins; [
  #yankring
  auto-pairs
  lsp-zero-nvim
  mason-nvim
  mason-lspconfig-nvim
  mason-tool-installer-nvim
  harpoon2
  vim-nix
  #{ plugin = vim-startify;
  #  config = "let g:startify_change_to_vcs_root = 0";
  #}
];
	};
}
