node {

    checkout scm

    env.DOCKER_API_VERSION="1.39"

    sh "git rev-parse --short HEAD > commit-id"

    tag = readFile('commit-id').replace("\n", "").replace("\r", "")
    tag = "latest"
    appName = "jenkinsapp1"
    registryHost = "dganitch/"
    imageName = "${registryHost}${appName}:${tag}"
    env.BUILDIMG=imageName

    stage "Build"

        sh "docker build -t ${imageName} -f Dockerfile ."

    stage "Push"

        sh "docker push ${imageName}"

    stage "Deploy"

        sh "kubectl delete -f deployment.yaml"
        sh "kubectl apply -f deployment.yaml"

}
