return {
  "williamboman/mason.nvim",
  dependencies = {
    "williamboman/mason-lspconfig.nvim",
    "WhoIsSethDaniel/mason-tool-installer.nvim",
  },
  config = function()
    local mason = require("mason")                     -- import mason
    local mason_lspconfig = require("mason-lspconfig") -- import mason-lspconfig
    local mason_tool_installer = require("mason-tool-installer")

    mason.setup({
      ui = {
        icons = {
          package_installed = "✓",
          package_pending = "➜",
          package_uninstalled = "✗",
        },
      },
    })

    mason_lspconfig.setup({
      -- list of servers for mason to install
      ensure_installed = {
        "rust_analyzer",
        "ltex-ls",
      },
    })

    mason_tool_installer.setup({
      ensure_installed = {
        "isort", -- python formatter
        "black",
        "rustfmt",
      },
    })
  end,
}
