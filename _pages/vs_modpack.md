---
title: VS Modpack
layout: default
permalink: /vintage-story
---

|      |                                                                              |
| ---- | ---------------------------------------------------------------------------- |
| 1234 | {{ site.data.fetched_mods \| where: "id", 1234 \| first \| dig: "version" }} |
