% Solfège Patterns in C major (do–mi, do–so, stepwise)
\version "2.24.0"
\header {
  title = "Solfège Patterns"
  subtitle = "C Major"
}

patterns = \relative c' {
  \key c \major
  \time 4/4
  c4 e g e | c2 r2 % do-mi-so-mi
  c4 d e f | g2 r2 % stepwise up
  g4 f e d | c2 r2 % stepwise down
  c4 g c g | c2 r2 % do-so-do-so
}

\score {
  \new Staff { \clef treble \patterns }
  \layout { }
  \midi { }
}

