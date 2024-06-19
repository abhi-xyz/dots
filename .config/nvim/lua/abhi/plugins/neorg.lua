return {
  {
    "vhyrro/luarocks.nvim",
    priority = 1000,
    config = true,
  },
  {
    "nvim-neorg/neorg",
    dependencies = {
      "nvim-neotest/nvim-nio",
      "MunifTanjim/nui.nvim",
      "pysan3/pathlib.nvim",
      "luarocks.nvim",
      "nvim-neorg/lua-utils.nvim",
    },
    lazy = false, -- Disable lazy loading as some `lazy.nvim` distributions set `lazy = true` by default
    version = "*", -- Pin Neorg to the latest stable release
    config = true,
  },
}
