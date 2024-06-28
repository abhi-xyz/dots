{ config, pkgs, ... }:


{
  home.username = "abhi";
  home.homeDirectory = "/home/abhi";
  home.stateVersion = "24.05";
  nixpkgs.config.allowUnfree = true;
  imports = [
    ./emacs.nix
    ./firefox.nix
  ];

  # Enable experimental features
  #nix = {
    #package = pkgs.nixUnstable;
    #extraOptions = "experimental-features = nix-command flakes";
  #};

  home.packages = with pkgs; [
    dunst
    #ffmpeg-full
    htop
    #kitty
    librewolf
    #libreoffice
    lxappearance
    newsboat
    (nerdfonts.override { fonts = [ "FantasqueSansMono" ]; })
    ripgrep
    spotify
    telegram-desktop
    wget
    unzip
    vlc
	xclip

    # fonts
    iosevka
    maple-mono

    # (pkgs.writeShellScriptBin "my-hello" ''
    #   echo "Hello, ${config.home.username}!"
    # '')
  ];

  # basic configuration of git, please change to your own
  programs.git = {
    enable = true;
    userName = "abhi";
    userEmail = "ugabhi@proton.me";
  };
  

  # Home Manager is pretty good at managing dotfiles. The primary way to manage
  # plain files is through 'home.file'.
  home.file = {
    # # Building this configuration will create a copy of 'dotfiles/screenrc' in
    # # the Nix store. Activating the configuration will then make '~/.screenrc' a
    # # symlink to the Nix store copy.
    # ".screenrc".source = dotfiles/screenrc;

    # # You can also set the file content immediately.
    # ".gradle/gradle.properties".text = ''
    #   org.gradle.console=verbose
    #   org.gradle.daemon.idletimeout=3600000
    # '';
  };

  # Home Manager can also manage your environment variables through
  # 'home.sessionVariables'. These will be explicitly sourced when using a
  # shell provided by Home Manager. If you don't want to manage your shell
  # through Home Manager then you have to manually source 'hm-session-vars.sh'
  # located at either
  #
  #  ~/.nix-profile/etc/profile.d/hm-session-vars.sh
  #
  # or
  #
  #  ~/.local/state/nix/profiles/profile/etc/profile.d/hm-session-vars.sh
  #
  # or
  #
  #  /etc/profiles/per-user/abhi/etc/profile.d/hm-session-vars.sh
  #
  home.sessionVariables = {
    EDITOR = "nvim";
    TERMINAL = "alacritty";
  };

  programs.home-manager.enable = true;
}
