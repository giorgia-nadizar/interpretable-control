---
layout: default
---

Check out the competition details below :point_down: 
and be sure to join our Discord server [https://discord.gg/dA8jpFVa9t](https://discord.gg/dA8jpFVa9t) for questions or news :loudspeaker:

# Motivation
Control systems play a vital role in managing and regulating various processes and devices across diverse application domains. 
Their pervasive nature makes them a cornerstone of modern technology. 
Safety-critical applications, in particular, demand control systems that are not only efficient but also interpretable, ensuring trustworthiness, reliability, and accountability.
However, a prevalent issue in the field is the over-reliance on opaque systems, such as deep neural networks, known for their efficiency and optimization potential. 
This preference is rooted in the prevailing belief that interpretability is of secondary importance, with performance taking precedence. 
Furthermore, the scarcity of objective metrics to assess the degree of interpretability in a system exacerbates this problem. 
In fact, though the Evolutionary Computation (EC) community is starting to promote explainable and/or interpretable AI, significant challenges still persist in achieving comprehensive solutions.
The goal of this competition is thus to ignite the research domain of interpretable control, with two specific goals in mind. 
First, we want to create a basis of comparison for different techniques emphasizing the trade-offs between performance and interpretability. 
Second, through the involvement of a panel of human evaluators, we strive to uncover the key characteristics that enhance the interpretability of control policies, making them more accessible to the general user.

# Tasks
We have chosen two tasks: [**Walker2D**](https://gymnasium.farama.org/environments/mujoco/walker2d/) for continuous control, 
and [**2048**](https://en.wikipedia.org/wiki/2048_(video_game)) for discrete control.
We provide details and examples for both tasks in the [competition repository](https://github.com/giorgia-nadizar/interpretable-control-competition).
For both tasks we set a limit of **200000** episodes for optimizing the policies.
An episode is a simulation of 1000 steps for Walker2D and a game for 2048.

# Participation
Participants can take part in **either or both** of the tracks.
Participants will have the freedom to apply their preferred methods to generate and interpret policies that effectively address the proposed task. 
However, we promote the inclusion of EC techniques into either the policy generation or explanation process, as a valuable component of addressing the proposed task.

Each submission will have to include the following:
- **Control policy score, explanation, and pipeline description**: a document
    - containing the score obtained by the policy, an interpretability analysis of the policy (covering all
      relevant information deducible from it), and the pipeline used to obtain it
    - of up to 2 pages in the [Gecco format](https://gecco-2024.sigevo.org/Call-for-Papers), excluding references
- **Control policy and code**: for reproducibility and assessment purposes, we require
    - _updated environment file_ or _additional requirements_ needed to make the code work
    - _run file_, i.e., a Python script, from which the submitted policy can be assessed on the environment
    - _optimization file_, i.e., a Python script, from which the optimization process can be reproduced
    - _optimization log_ reporting the progression of the policies scores during the performed optimization
 
All submission files will have to be uploaded to a github repository. The submission will then have to be made through the following form: [https://forms.gle/bUKLKmKRGQ1niNZm7](https://forms.gle/bUKLKmKRGQ1niNZm7)

If you want to ask any question or provide some feedback, join us at our Discord server: [https://discord.gg/dA8jpFVa9t](https://discord.gg/dA8jpFVa9t).

# Submission deadline
20th June 2024 AoE.

~~13th June 2024 AoE.~~

# Evaluation criteria
The final score for each entry will be determined by combining the two following terms.
- Performance Rank: this will be evaluated by simulating the submitted policy to assess its effectiveness in solving the given problem.
- Interpretability Rank: this aspect will be appraised by a panel of judges. The guidelines provided to the jury will include the following considerations:
  - Clarity of the pipeline
  - Readability of the model
  - Clarity of the explanation provided
  - Amount of processing required to derive the explanation from the raw policy

These two ranks will be combined using the geometric mean to compute the overall global rank for each competition entry.

# Results and dissemination
Our objective is to raise awareness regarding the importance of interpretability within the realm of control systems. 
To achieve this, we aim at collecting a wide variety of methodologies and publishing the results in a comprehensive report. 
We also plan to extend an invitation to select participants to become co-authors of this publication.

# Prize
The winner(s) will be awarded a certificate and a cash prize (totaling 1000€) sponsored by [Aindo](https://www.aindo.com/).

# Organizers
**Giorgia Nadizar**, University of Trieste, [giorgia.nadizar@phd.units.it](mailto:giorgia.nadizar@phd.units.it) <br>
Giorgia Nadizar is a third year PhD student at the University of Trieste, Italy. 
Her research interests lie at the intersection of embodied AI and explainable/interpretable AI.


**Luigi Rovito**, University of Trieste, [luigi.rovito@phd.units.it](mailto:luigi.rovito@phd.units.it ) <br>
Luigi Rovito is a third year PhD student at the University of Trieste, Italy. 
His research interests are genetic programming for cryptography and interpretable ML.


**Dennis G. Wilson**, ISAE-SUPAERO, University of Toulouse, [dennis.wilson@isae.fr](mailto:dennis.wilson@isae.fr) <br>
Dennis G. Wilson is an Associate Professor at ISAE-Supaero in Toulouse, France. 
They research evolutionary algorithms, deep learning, and applications of AI to climate problems.

**Eric Medvet**, University of Trieste, [emedvet@units.it](mailto:emedvet@units.it) <br>
Eric Medvet is an Associate Professor at the University of Trieste, Italy. 
His research interests include embodied AI, artificial life, and evolutionary optimization.

# Sponsors
[<img src="https://github.com/giorgia-nadizar/interpretable-control-competition/assets/74328581/ba96b53f-1018-486a-959a-690f0cb8a84d">](https://www.aindo.com/)
