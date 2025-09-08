% Yankee Doodle - Melody in C major
\version "2.24.0"
\header {
  title = "Yankee Doodle"
  subtitle = "Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  c4 c d e | c e d2 |
  c4 c d e | c e d2 |
  e4 f g e | f g a2 |
  g4 g f e | d c c2 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

