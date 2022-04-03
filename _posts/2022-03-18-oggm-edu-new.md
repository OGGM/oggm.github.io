---
layout: post
title: A new modelling interface for OGGM-Edu
subtitle: Glacier modeling made even easier
author: Erik Holmgren
date: 2022-03-18T00:00:00
tags: oggm-edu
---

During the last few months we've been working on a new interface for the OGGM-Edu notebooks. 
Our goal is to provide students and educators with an easy and intuitive way to interact and experiment with 
OGGM, even with limited coding experience. 

**Today, we are very happy to announce that this new interface is ready to be used!** 
See its tools documented [here](https://edu.oggm.org/en/latest/api.html) or, even better, 
see them in action on the [OGGM-Edu notebooks page](https://oggm.org/oggm-edu-notebooks).

The `oggm-edu` python package now ships five entirely new classes:
- `Glacier`: the main way to evolve and plot a glacier
- `SurgingGlacier`: similar to `Glacier`, but surging!
- `GlacierBed`: makes it easy to create linear and non-linear glacier bed.
- `Massbalance`: create a simple (or complex!) mass balance profile for the `Glacier`.
- `GlacierCollection`: a storage container for multiple `Glaciers`, making it possible to perform experiments on multiple glaciers.

Creating a glacier is now very simple! We have also improved the plotting routines greatly:

```python
from oggm_edu import MassBalance, GlacierBed, Glacier

# Create the bed

bed = GlacierBed(top=3400, bottom=1500, width=300)
# And the mass balance

mass_balance = MassBalance(ela=3000, gradient=4)
# And finally the glacier!

glacier = Glacier(bed=bed, mass_balance=mass_balance)
glacier.plot()
```
<img src="/img/blog/oggm-edu-new/edu_intro_26_0.png" alt="" width="100%"/>

To grow the glacier there we can either progress the glacier to a specified year:


```python
glacier.progress_to_year(150)
glacier.plot()
```
<img src="/img/blog/oggm-edu-new/edu_intro_31_0.png" alt="" width="100%"/>


Or progress the glacier to equilibrium:


```python
glacier.progress_to_equilibrium()
glacier.plot()
```
<img src="/img/blog/oggm-edu-new/edu_intro_37_0.png" alt="" width="100%"/>


It is just as easy to inspect the history of the length, volume and area of the glacier:

```python
glacier.plot_history()
```
<img src="/img/blog/oggm-edu-new/edu_intro_43_0.png" alt="" width="100%"/>

This is just a small part of what is possible with the new interface.
We hope that you will find this interesting, and are waiting for your feedback!
