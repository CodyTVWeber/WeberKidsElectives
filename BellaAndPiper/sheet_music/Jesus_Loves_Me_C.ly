% Jesus Loves Me - Melody in C major (public domain hymn)
\version "2.24.0"
\header {
  title = "Jesus Loves Me"
  subtitle = "Melody (C Major)"
  composer = "W. B. Bradbury"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  e4 e f g | g g g2 |
  a4 a g f | e2 e |
  e4 e f g | g g g2 |
  a4 a g f | e1 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

