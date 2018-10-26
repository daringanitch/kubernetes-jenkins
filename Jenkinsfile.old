node {

    checkout scm

    env.DOCKER_API_VERSION="1.39"

    sh "git rev-parse --short HEAD > commit-id"

    tag = readFile('commit-id').replace("\n", "").replace("\r", "")
    tag = "latest"
    appName = "jenkinsapp"
    registryHost = "claudioacquaviva/"
    imageName = "${registryHost}${appName}:${tag}"
    env.BUILDIMG=imageName

    stage "Build"

        sh "docker build -t ${imageName} -f Dockerfile ."

    stage "Push"

        sh "docker push ${imageName}"

    stage "Deploy"

        sh "kubectl set image deployments/jenkinsapp jenkinsapp=claudioacquaviva/jenkinsapp"

}
