% Row, Row, Row Your Boat - Melody and round entry in C major
\version "2.24.0"
\header {
  title = "Row, Row, Row Your Boat"
  subtitle = "Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  c4 c c d | e2 e |
  e4 d e f | g2 g |
  a4 a a g | f2 f |
  e4 e d d | c1 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

