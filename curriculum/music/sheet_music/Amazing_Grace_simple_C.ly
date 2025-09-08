% Amazing Grace - Simple melody in C major
\version "2.24.0"
\header {
  title = "Amazing Grace"
  subtitle = "Simple Melody (C Major)"
  composer = "Traditional / J. Newton"
}

melody = \relative c' {
  \key c \major
  \time 3/4
  c4 e g | a2 g4 | a g e | g2. |
  c,4 e g | a2 g4 | a g e | c2. |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

