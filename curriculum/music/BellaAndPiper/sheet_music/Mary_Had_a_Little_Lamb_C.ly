% Mary Had a Little Lamb - Melody in C major
\version "2.24.0"
\header {
  title = "Mary Had a Little Lamb"
  subtitle = "Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  e4 d c d | e e e2 |
  d4 d d2 | e4 g g2 |
  e4 d c d | e e e e |
  d4 d e d | c1 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

