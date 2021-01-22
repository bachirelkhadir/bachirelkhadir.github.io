;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")
;;; (hack-dir-local-variables)

((markdown-mode . ((eval . (defun now nil "Insert string for the current time formatted like '2:34 PM'."
                                  (interactive)
                                  (insert
                                   (format-time-string "%Y-%m-%d %H-%M-%S"))))))
 (prog-mode . ((projectile-project-compilation-cmd . "bundle exec jekyll serve --livereload"))))
