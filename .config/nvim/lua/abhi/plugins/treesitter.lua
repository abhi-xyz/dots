-- TODO: setup auto install

return {
  "nvim-treesitter/nvim-treesitter",
  event = { "BufReadPre", "BufNewFile" },
  build = ":TSUpdate",
  dependencies = {
    "hiphish/rainbow-delimiters.nvim",
    "windwp/nvim-autopairs",
    "windwp/nvim-ts-autotag",
  },
  config = function()
    -- import nvim-treesitter plugin
    local treesitter = require("nvim-treesitter.configs")

    -- configure treesitter
    treesitter.setup({
      highlight = { enable = true },
      indent = { enable = true },
      autotag = {
        enable = true,
      },
      sync_install = true,
      auto_install = true,

      ensure_installed = {
        "bash",
        "c",
        "go",
        "gitignore",
        "json",
        "html",
        "lua",
        "nix",
        --"org",
        "python",
        "rust",
        "rasi",
        "sxhkdrc",
        "ssh_config",
        "toml",
        "vim",
        "yaml",
        "zathurarc",
      },
      ignore_install = { 'org' },
      incremental_selection = {
        enable = true,
        keymaps = {
          init_selection = "<C-space>",
          node_incremental = "<C-space>",
          scope_incremental = false,
          node_decremental = "<bs>",
        },
        autotag = {
          enable = true,
        },
        autopairs = {
          enable = true,
        },

        rainbow = {
          enable = true,
        },
      },
    })
  end,
}
