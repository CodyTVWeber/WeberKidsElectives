% Frère Jacques - Melody with round annotation in C major
\version "2.24.0"
\header {
  title = "Frère Jacques"
  subtitle = "Melody (C Major) — Round"
  composer = "Traditional"
}

melody = \relative c' {
  \key c \major
  \time 4/4
  c4 d e c | c d e c |
  e f g2 | e f g2 |
  g a g f | e c2. |
  g a g f | e c2. \bar "|." |
}

\score {
  \new Staff { \clef treble \melody }
  \layout { }
  \midi { }
}

