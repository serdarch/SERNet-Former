layers = [
    sequenceInputLayer(numFeatures)
    lstmLayer(hiddenSize, 'OutputMode', 'last')
    fullyConnectedLayer(numClasses)
    softmaxLayer
    classificationLayer
];
