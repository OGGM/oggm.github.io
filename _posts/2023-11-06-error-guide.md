---
layout: post
title: Help, an error! 
subtitle: A short guide on what to do once you get stuck or have other question
author: Anouk Vlug and Jenna Sutherland
date: 2023-11-06T00:00:00
tags: Community Programming Model
---

When you start using OGGM it is very likely that you will have many questions and it is inevitable that you will receive 
an error at some point when running your script. Over time we have noticed that, especially for those of you who are new 
to OGGM and coding in general, it can be hard to deal with this efficiently. Some struggle needlessly for a long time by 
themselves, while others ask such an overload of questions that it becomes tiring for the community. Some of you might 
even panic at the sight of an error, even though there is an abundance of resources around to help you. Please don’t 
worry, we’re going to guide you step-by-step through what to do when an error occurs or a question arises.

## Try to find the solution yourself
The first step is to try to find the solution yourself. You can, for instance,
- read the [documentation](https://docs.oggm.org/en/stable/),
- go through the [tutorials](https://oggm.org/tutorials/stable/notebooks/welcome.html),
- checkout the doc string (ADD link) of the function you might be trying to use or search for the function description 
in the [List of OGGM functions and tasks](https://docs.oggm.org/en/stable/api.html),
- and look more into depth at the code you’re trying to use and try some debugging.
- In some cases it might make sense to have a look at the publication [list](https://oggm.org/publications/),
- [OGGM-edu](https://edu.oggm.org/en/latest/),
- check-out the [blog posts](https://oggm.org/search/index.html)
- or search for a solution by using a search engine.

## Asking a question
If you haven’t succeeded in finding the answer yourself after having made a serious attempt to find it, it might be the 
right time to ask a question. OGGM luckily has an active community that can help you further. As members of the 
community answer questions on a voluntary basis, please be kind to them, don’t overload them, and ask questions in a way 
that are easy to understand. The latter point is especially important when you're relatively new to programming. The 
following sections will take you through  where to ask your question, how to ask your question, manage your expectations 
and close the question/issue once it has been solved.

### Where to ask your question
Generally no OGGM coding support is given by e-mail. Most questions are best asked in the #support channel on the OGGM 
[Slack](https://oggm.org/2022/10/11/Welcome-to-the-OGGM-Slack/), our internal communications platform. That is where you 
will most likely get the fastest response. However if you, for instance, have many questions or would rather talk about 
the issue, you’re more than welcome to join the fortnightly on-line [community meetings](https://oggm.org/meetings/). 
Only if you are working on code development or in case of a bug in the code base, then the 
[github](https://github.com/OGGM/) might be the most suitable place for raising an 
[issue](https://github.com/OGGM/oggm/issues).

### How to ask your question
Now you have chosen where you’re going to ask your question. It would be good if you do a quick check to see if the 
question has already been asked. It may sound obvious and straightforward to ask a clear question, but it requires a bit 
of effort and is harder than it might seem. The “I got error XXX, how do I solve this?” type of question without any 
context is as impossible to answer as “I’m not where I want to be, can you solve this?”. For colleagues to be able to 
help you, you need to give context and as much detail as possible, so the question turns into something answerable. You 
should present the details together with the question you post, which many people do not often understand or realize. 
Therefor we list the order of items below, including an everyday example to illustrate why the different items are 
important:

<DL>
<DT> What would you like/are you trying to do
    <DD> e.g. I’m trying to do global glacier projections for the coming century (I would like to enter the seminar room)
<DT> Why you would like to do that
    <DD> e.g. because I would like to test what the influence of feature X is on the projections once I have added my own 
      module (to check if I can connect my laptop, before my presentation next week)
<DT> How are you trying to do this
    <DD> e.g. the python code I’m using (so I went to the seminar room.)
<DT> Why is this is not working
    <DD> e.g. the full error log (However the room is closed and I don’t have a key.)
<DT> What have you already tried to solve this
    <DD> e.g. I have used the following tutorials to try to find the answer (I asked the secretary and the concierge for a key, 
      but they don’t have one either.)
<DT> Ask the question
    <DD> e.g. does anyone know how to solve this error? (Can someone help me get into the seminar room?)
</DL>

Omitting parts can leave people wondering what you’re talking about or lead to answers that are useless to you (as you 
might get advice that you already tried and it didn’t work or suggestions that don’t fulfill your needs). In addition, 
the solutions that could solve your issue might not be shared if you fail to mention everything. Depending on the 
motivation it might be useful to know that for the specifc example above, OGGM has provided 
[standard projections](https://docs.oggm.org/en/stable/download-projections.html) (or your colleague knows all adapters 
available in the seminar room). So, to summarize: leaving out essential details can waste both your time and that of 
your colleagues.

### The reply
Once you have asked the question, it is time to wait for a reply. This generally speaks for itself. Just be patient, 
people answer these questions voluntarily and have different working hours and cultures. e.g. don’t be surprised if your 
question doesn’t get answered during the weekend. In addition, please let us know if the issue gets solved in the 
meantime. 

On Slack, the conversation regarding a question takes place in the thread to keep things organized and on github this 
happens within the respective issue that has been opened. In both cases please make it clear once a solution has been 
found. On the github you can close your issue in such a case. On Slack you can add a checkmark to the main question, 
using e.g. the ✅ emoji (you will see what is meant when scrolling through the support channel), so that the others know 
the question has been answered and won’t lose time reading the whole thread when offering their help. It goes without 
saying that it is always welcome to thank people for helping you and offer help when you can 😉
