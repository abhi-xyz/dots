{
  programs.emacs = {
    enable = true;
    extraPackages = epkgs: with epkgs; [
      auto-complete
      company
      counsel
      dashboard
      doom-modeline
      doom-themes
      evil
      evil-collection
      flycheck
      general
      hl-todo
      ivy
      magit
      nix-mode
      org-modern
      python-mode
      projectile
      pdf-tools
      use-package
    ];
    extraConfig =''

      ;; changing some defaults
      (scroll-bar-mode -1)         ;; Disable the scroll bar
      (menu-bar-mode -1)           ;; Disable the menu bar 
      (tool-bar-mode -1)           ;; Disable the tool bar
      (delete-selection-mode 1)    ;; You can select text and delete it by typing.
      (electric-indent-mode -1)    ;; Turn off the weird indenting that Emacs does by default.
      (electric-pair-mode 1)       ;; Turns on automatic parens pairing
      ;; The following prevents <> from auto-pairing when electric-pair-mode is on.
      ;; Otherwise, org-tempo is broken when you try to <s TAB...
      (add-hook 'org-mode-hook (lambda ()
                                (setq-local electric-pair-inhibit-predicate
                                 `(lambda (c)
                                   (if (char-equal c ?<) t (,electric-pair-inhibit-predicate c))))))
      (global-auto-revert-mode t)  ;; Automatically show changes if the file has changed
      (global-display-line-numbers-mode 1) ;; Display line numbers
      (global-visual-line-mode t)  ;; Enable truncated lines
      (setq org-edit-src-content-indentation 0) ;; Set src block automatic indent to 0 instead of 2.
      (setq use-file-dialog nil)   ;; No file dialog
      (setq use-dialog-box nil)    ;; No dialog box
      (setq pop-up-windows nil)    ;; No popup windows
      (setq display-line-numbers-type 'relative)


      ;; evil

      (setq evil-want-integration t  ;; This is optional since it's already set to t by default.
       evil-want-keybinding nil
       evil-vsplit-window-right t
       evil-split-window-below t
       evil-undo-system 'undo-redo)  ;; Adds vim-like C-r redo functionality
      (evil-mode)
      ;;(add-to-list 'evil-collection-mode-list 'help) ;; evilify help mode
      (evil-collection-init)

        (dashboard-setup-startup-hook)
        ;; fonts

        (set-face-attribute 'default nil
         :font "Maple Mono"
         :height 110
         :weight 'medium)
        (set-face-attribute 'variable-pitch nil
         :font "Maple Mono"
         :height 120
         :weight 'medium)
        (set-face-attribute 'fixed-pitch nil
         :font "Maple Mono"
         :height 110
         :weight 'medium)
        ;; Makes commented text and keywords italics.
        ;; This is working in emacsclient but not emacs.
        ;; Your font must have an italic face available.
        (set-face-attribute 'font-lock-comment-face nil
         :slant 'italic)
        (set-face-attribute 'font-lock-keyword-face nil
         :slant 'italic)

        ;; This sets the default font on all graphical frames created after restarting Emacs.
        ;; Does the same thing as 'set-face-attribute default' above, but emacsclient fonts
        ;; are not right unless I also add this method of setting the default font.
        (add-to-list 'default-frame-alist '(font . "Maple Mono-11"))

        ;; Uncomment the following line if line spacing needs adjusting.
        (setq-default line-spacing 0.12)

        (global-set-key (kbd "C-=") 'text-scale-increase)
        (global-set-key (kbd "C--") 'text-scale-decrease)
        (global-set-key (kbd "<C-wheel-up>") 'text-scale-increase)
        (global-set-key (kbd "<C-wheel-down>") 'text-scale-decrease)
        
        ;; modeline

        (doom-modeline-mode 1)
        (setq doom-modeline-height 35      ;; sets modeline height
        doom-modeline-bar-width 5    ;; sets right bar width
        doom-modeline-persp-name t   ;; adds perspective name to modeline
        doom-modeline-persp-icon t)

        ;; org
        (custom-set-faces
         ;; custom-set-faces was added by Custom.
         ;; If you edit it by hand, you could mess it up, so be careful.
         ;; Your init file should contain only one such instance.
         ;; If there is more than one, they won't work right.
         '(org-level-1 ((t (:inherit outline-1 :height 1.7))))
         '(org-level-2 ((t (:inherit outline-2 :height 1.6))))
         '(org-level-3 ((t (:inherit outline-3 :height 1.5))))
         '(org-level-4 ((t (:inherit outline-4 :height 1.4))))
         '(org-level-5 ((t (:inherit outline-5 :height 1.3))))
         '(org-level-6 ((t (:inherit outline-5 :height 1.2))))
         '(org-level-7 ((t (:inherit outline-5 :height 1.1)))))

        (require 'org-tempo)

        ;; Add frame borders and window dividers
        (modify-all-frames-parameters
         '((right-divider-width . 40)
           (internal-border-width . 40)))
        (dolist (face '(window-divider
                        window-divider-first-pixel
                        window-divider-last-pixel))
         (face-spec-reset-face face)
         (set-face-foreground face (face-attribute 'default :background)))
        (set-face-background 'fringe (face-attribute 'default :background))

        (setq
         ;; Edit settings
         org-auto-align-tags nil
         org-tags-column 0
         org-catch-invisible-edits 'show-and-error
         org-special-ctrl-a/e t
         org-insert-heading-respect-content t

         ;; Org styling, hide markup etc.
         org-hide-emphasis-markers t
         org-pretty-entities t

         ;; Agenda styling
         org-agenda-tags-column 0
         org-agenda-block-separator ?─
         org-agenda-time-grid
         '((daily today require-timed)
           (800 1000 1200 1400 1600 1800 2000)
           " ┄┄┄┄┄ " "┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄")
         org-agenda-current-time-string
         "◀── now ─────────────────────────────────────────────────")

         ;; Ellipsis styling
         (setq org-ellipsis "…")
         (set-face-attribute 'org-ellipsis nil :inherit 'default :box nil)

         (global-org-modern-mode)

        (setq org-src-preserve-indentation t)


        ;;themes

        (load-theme 'doom-tokyo-night t)

        (setq doom-themes-enable-bold t    ; if nil, bold is universally disabled
         doom-themes-enable-italic t) ; if nil, italics is universally disabled
        ;; Sets the default theme to load!!! 
        ;;(load-theme 'doom-one t)
        ;; Enable custom neotree theme (all-the-icons must be installed!)
        (doom-themes-neotree-config)
        ;; Corrects (and improves) org-mode's native fontification.
        (doom-themes-org-config)

        (setq standard-indent 2)
      '';
    
  };
}
