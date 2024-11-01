{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "pygame-dev"; # This will show in your prompt

  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.virtualenv
    python311Packages.pygame
  ];
  
  shellHook = ''
    # Create and activate virtual environment
    VENV=.venv
    if [ ! -d "$VENV" ]; then
      echo "Creating virtual environment..."
      virtualenv $VENV
    fi
    source $VENV/bin/activate
    
    # Install requirements if requirements.txt exists
    if [ -f requirements.txt ]; then
      echo "Installing requirements..."
      pip install -r requirements.txt
    fi

    # Your preferred shell
    export SHELL=${pkgs.fish}/bin/fish
    exec fish
  '';
}
