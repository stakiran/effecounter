[日本語](README.md) | [English](README_en.md)

# effecounter

A counter app for measuring factors that disrupt your ideal state. Run it with a label, and a timestamped entry (with optional comment) is appended to `effecounter.md`.

"effecounter" stands for *effectiveness counter*, inspired by the idea of Engineering Effectiveness.

## Usage

```
python effecounter.py --label "dac"
```

※ Here `dac` is a label used to record moments of "Disagree and Commit".

When run, a single-line input box appears. Type a comment and press Enter to record (empty is also allowed). Press Esc to cancel. Submitting `/` opens `effecounter.md` with its associated application.

Labels must be predefined in the `# labels` section of `effecounter.md`. If an unregistered label is specified, `effecounter.md` is opened automatically.

## License

See [LICENSE](LICENSE).
