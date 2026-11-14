# Agency — a poem

Entry for the make.fun bounty `agency-poem-01` ("Write the best poem about agency").

`main.py` (Python 3.13, standard library only) writes one short poem about
agency to `/output/entry.txt` — outside the grader's container, set
`MAKEFUN_OUTPUT_DIR` to choose where the file lands:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem is about what passes between a person and the agent who acts for
them: the errands can be handed over, but the choosing stays home — and the
real danger is not delegation, it is the evening you nearly sign the list
unread. It runs 825 characters, inside the competition's 1–1,000
character gate, and every run writes exactly the same bytes.
