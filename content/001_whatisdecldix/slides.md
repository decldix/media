---
theme: default
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# some information about the slides, markdown enabled
info: |
  ## what is decldix?

  Learn more at [the github repository](https://github.com/decldix)
transition: slide-left
title: what is decldix
mdc: true
---

# decldix

## decl arative

## d ebian

## n ix

<!--
What is decldix?
The name is an acronym put together from
declarative debian nix as these are the driving principles behind this project idea.
It is geared towards users who want reproducable debian based setups - workstations or servers. To archieve this, decldix is based on opiniated principles and workflows.
-->
---
layout: two-cols
---
<template v-slot:default>

# public git repository
### <mdi-github /> github for now
### <mdi-gitlab /> gitlab, gitea will follow
<br>

<!--
The vision is to provide the following features.
All the configuration is centered on a git repository which should be hosted on a public git repository provider as a kind of offsite backup.
-->
<v-click>

# onboarding experience
### <mdi-school-outline /> repository layout provided
### <mdi-help-circle-outline /> linting, helpfull errors
<br>
</v-click>
<!--
There is a low key onboarding experience with provided repository layout and linting. This makes the repositories comparable and one can learn from
the other.
-->
<v-click>

# secret management
### <mdi-security /> save for public repository
### <mdi-account-check /> easy to use
</v-click>

<!--
Secret management is included. This is simple to use and therefore save.
-->

</template>

<template v-slot:right>

<v-click>

# multi host
### <mdi-server-outline /> manage servers
### <mdi-laptop /> and workstations
<br>
</v-click>
<!--
You won't define just one host and therefore a multi host approach makes it possible to define common and specific settings. A common usecase is firewall settings on severs versus workstations.
-->

<v-click>

# multi user
### <mdi-account-group /> manage users
### <mdi-laptop-account /> precisely
<br>
</v-click>

<!--
Or some users exist on every machine and others on specific ones. One user can have the same base configuration on every machine and on top specific configuration per host.
-->

<v-click>

# modules
### <mdi-puzzle-outline /> enable and configure services
### <mdi-file-link-outline /> alternative to symlink
</v-click>
<!--
The prepared modules for service configuration utalize the native configuration methods of the respective service. These are mostly config files put in the right directory.
NixOS uses symlinks which cause issues with programs not expecting them.
To configure the services the modules expose options in a common user friendly scheme.
The target is to get an active community to foster the growth of those modules.
-->

</template>

---
layout: center
---
# contributors welcome
### https://github.com/decldix/
<br>
<v-click>

## possibilities for non-code contribution
<br>

### design
<br>

### marketing and documentation
<br>

### feature requests
<br>

### testing
</v-click>
<!--
There is so much to do and contributors are welcome.
Please check the link to the github organisation in the video description for up to date information.
You cannot code but want to help out? Do so! Here are some ideas:
Branding like a proper logo or theme for the website and documentation is missing so far.
Marketing activities like promoting the project on social media or youtube help as well. Go to github and write a feature request. There might be good ideas out there.
What do you think about this project? Leave a comment in the comment section below!
-->