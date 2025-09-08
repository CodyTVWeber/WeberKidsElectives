% Skip to My Lou - Melody in C major
\version "2.24.0"
\header {
  title = "Skip to My Lou"
  subtitle = "Melody (C Major)"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 2/4
  c8 c c c | d d e e | g4 e | d2 |
  c8 c c c | d d e e | g4 e | d2 \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

