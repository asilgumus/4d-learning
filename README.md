# 4d learning

4d learning is a small open education platform created by frc team 6429, 4th dimension.

we built it to make our stem projects easier to understand, reuse, and adapt. the platform currently includes guides for neurobridge, e-parenting 4 stem, lego mri, cybersecurity, and a collection of nineteen arduino experiments. a technology addiction workshop will be added later.

the website is intentionally simple. it uses plain html, css, and javascript, so there is no framework or build step to worry about.

## running it locally

```sh
npm run dev
```

then open `http://localhost:4173` in your browser.

## checking the content

```sh
npm run check
```

this checks the javascript files, learning track data, arduino lessons, and local resource files.

## adding a new guide

learning tracks and lesson content live in `data.js`. add the source file under `assets/resources`, create or update the related project record, and follow the same section structure used by the existing guides.

## about the team

4th dimension is frc team 6429 from izmir, türkiye. we share these materials so other teams, schools, and community groups can build on what we have learned.
