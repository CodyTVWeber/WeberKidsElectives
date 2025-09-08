% Home on the Range - Melody in C major (public domain)
\version "2.24.0"
\header {
  title = "Home on the Range"
  subtitle = "Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 3/4
  c4 e g | a2 g4 | f e d | c2. |
  g'4 g a | g2 e4 | f e d | c2. \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

