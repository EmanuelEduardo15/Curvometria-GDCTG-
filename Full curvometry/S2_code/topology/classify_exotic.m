function I_M = classify_exotic(kappa, R)
    % Input: 
    %   kappa = curvature vector
    %   R = radius vector
    I_M = trapz(kappa .* R);  % Compute invariant
    
    % Classification
    if abs(I_M) > 1e-6
        disp('Exotic 7-sphere detected (Invariant ≠ 0)');
    else
        disp('Standard 7-sphere (Invariant = 0)');
    end
end

% Example usage:
kappa = [0.1, 0.3, 0.5, 0.2];
R = 1./kappa;
classify_exotic(kappa, R);
