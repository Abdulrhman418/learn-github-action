const core = require('@actions/core');
const exec = require('@actions/exec');

function validateBranch(branch) {
  const regex = /^[\w.-/]+$/; 
  return regex.test(branch);
}

function validateDirectory(dir) {
  const regex = /^[\w-/]+$/; 
  return regex.test(dir);
}

async function run() {
  try {
    const baseBranch = core.getInput('base-branch');
    const targetBranch = core.getInput('target-branch');
    const workingDir = core.getInput('working-directory');
    const ghToken = core.getInput('gh-token');
    const debug = core.getBooleanInput('debug') || false;


    if (!validateBranch(baseBranch)) {
      core.setFailed(`Invalid base branch name: ${baseBranch}`);
      return;
    }
    if (!validateBranch(targetBranch)) {
      core.setFailed(`Invalid target branch name: ${targetBranch}`);
      return;
    }
    if (!validateDirectory(workingDir)) {
      core.setFailed(`Invalid working directory: ${workingDir}`);
      return;
    }

    console.log(`Base branch: ${baseBranch}`);
    console.log(`Target branch: ${targetBranch}`);
    console.log(`Working directory: ${workingDir}`);

    if (debug) console.log('Debug mode is ON');

    console.log('Running npm update...');
    await exec.exec('npm', ['update'], { cwd: workingDir });


    const { stdout } = await exec.getExecOutput('git', ['status', '-s', 'package*.json'], { cwd: workingDir });

    if (stdout.trim().length > 0) {
      console.log('Updates are available for package.json or package-lock.json!');
    } else {
      console.log('No updates available at this point in time.');
    }

  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
