# SCRIB-DL

This is a project for the students who might need it (including me)

> **Note:** the pages may or may not be in order, and may include the ad overlays, will patch

## what does it do?

You paste in the scribd url and it outputs a pdf in the `/screenshots` directory!

## how does it work?

It uses [playwright](https://playwright.dev/python/) and screenshots each page, then it uses [img2pdf](https://pypi.org/project/img2pdf/) to create a pdf
with those images

### acknowledgements!

- [example pdf used](https://www.scribd.com/document/870826699/Solution-to-CSEC-Math-Jan-2025-P1)
- [playwright](https://playwright.dev/python/)
- [img2pdf](https://pypi.org/project/img2pdf/)
