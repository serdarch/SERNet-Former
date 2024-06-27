hiddenSize = 100;
layers = [
    imageInputLayer([28 28 1])
    fullyConnectedLayer(hiddenSize)
    reluLayer
    fullyConnectedLayer(numClasses)
    softmaxLayer
    classificationLayer
];
