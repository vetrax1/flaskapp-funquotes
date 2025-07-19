@Library('jenkins-shared-lib') _

basePipeline([
  repoUrl: "https://github.com/vetrax1/flaskapp-funquotes.git",
  port: "5000",
  dockerImage: "anunukemsam/flaskapp-logger:${env.BUILD_NUMBER}"
])
