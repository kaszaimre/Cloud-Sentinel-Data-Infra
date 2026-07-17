const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const profileIcon = document.getElementById('profile-icon');
const profileName = document.getElementById('profile-name');
const profileHp = document.getElementById('profile-hp');
const profileMp = document.getElementById('profile-mp');
const profileRange = document.getElementById('profile-range');
const profileLevel = document.getElementById('profile-level');

const btnMove = document.getElementById('btn-move');
const btnAttack = document.getElementById('btn-attack');
const btnFortify = document.getElementById('btn-fortify');
const btnEndTurn = document.getElementById('btn-end-turn');
const btnRestart = document.getElementById('btn-restart');

const GRID_SIZE = 10;
let tileSize = 60;
let gridOffsetX = 0;
let gridOffsetY = 0;

let isPlayerTurn = true;
let selectedUnit = null;
let selectedAction = null;
let validMoves = [];
let validTargets = [];

const gameMap = [
  [0,0,1,0,0,3,0,0,0,0],
  [0,2,1,0,0,3,3,0,0,0],
  [0,2,0,0,0,0,3,0,0,0],
  [0,0,0,1,0,0,3,3,0,0],
  [0,0,0,1,1,0,0,3,0,0],
  [0,0,0,0,1,0,0,3,0,0],
  [0,0,1,0,0,0,3,3,0,0],
  [0,0,1,1,0,3,3,0,0,0],
  [0,0,0,0,0,3,0,0,2,0],
  [0,0,0,0,0,3,0,0,2,0]
];

function createUnits() {
  return [
    { id: 1, name: 'Borsodi Páncélos', owner: 'player', x: 2, y: 3, hp: 100, maxHp: 100, mp: 3, maxMp: 3, range: '1-2', level: 2, icon: '🚜', color: '#00ff66' },
    { id: 2, name: 'Sajó-völgyi Gyalogos', owner: 'player', x: 4, y: 6, hp: 100, maxHp: 100, mp: 2, maxMp: 2, range: '1', level: 1, icon: '🏃', color: '#00ff66' },
    { id: 3, name: 'Don Tüzérség', owner: 'enemy', x: 7, y: 5, hp: 100, maxHp: 100, mp: 1, maxMp: 1, range: '2-4', level: 3, icon: '💥', color: '#ff3366' },
    { id: 4, name: 'Ellenséges Páncélos', owner: 'enemy', x: 6, y: 8, hp: 100, maxHp: 100, mp: 3, maxMp: 3, range: '1-2', level: 2, icon: '🚜', color: '#ff3366' }
  ];
}

let units = createUnits();

function log(msg) {
  const logBox = document.getElementById('logBox');
  if (!logBox) return;
  const div = document.createElement('div');
  div.className = 'log-row system-log';
  div.textContent = `➔ ${msg}`;
  logBox.prepend(div);
}

function parseRange(range) {
  if (range.includes('-')) {
    const [min, max] = range.split('-').map(Number);
    return { min, max };
  }
  const n = Number(range);
  return { min: n, max: n };
}

function resizeCanvas() {
  const container = document.querySelector('.canvas-wrapper');
  if (!container) return;
  canvas.width = container.clientWidth;
  canvas.height = container.clientHeight;
  const minDim = Math.min(canvas.width, canvas.height);
  tileSize = Math.max(1, Math.floor((minDim - 20) / GRID_SIZE));
  gridOffsetX = Math.floor((canvas.width - tileSize * GRID_SIZE) / 2);
  gridOffsetY = Math.floor((canvas.height - tileSize * GRID_SIZE) / 2);
  draw();
}

function draw() {
  if (!ctx) return;
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let r = 0; r < GRID_SIZE; r++) {
    for (let c = 0; c < GRID_SIZE; c++) {
      const x = gridOffsetX + c * tileSize;
      const y = gridOffsetY + r * tileSize;
      const cellType = gameMap[r][c];
      ctx.fillStyle = cellType === 0 ? '#0b131a' : cellType === 1 ? '#0a231c' : cellType === 2 ? '#1c222a' : '#0b1e36';
      ctx.fillRect(x, y, tileSize, tileSize);
      ctx.strokeStyle = '#1a2936';
      ctx.strokeRect(x, y, tileSize, tileSize);
    }
  }

  if (selectedAction === 'move') {
    validMoves.forEach(m => {
      const x = gridOffsetX + m.x * tileSize;
      const y = gridOffsetY + m.y * tileSize;
      ctx.fillStyle = 'rgba(0,255,102,0.2)';
      ctx.fillRect(x + 2, y + 2, tileSize - 4, tileSize - 4);
    });
  }

  if (selectedAction === 'attack') {
    validTargets.forEach(t => {
      const x = gridOffsetX + t.x * tileSize;
      const y = gridOffsetY + t.y * tileSize;
      ctx.fillStyle = 'rgba(255,51,102,0.25)';
      ctx.fillRect(x + 2, y + 2, tileSize - 4, tileSize - 4);
    });
  }

  units.forEach(u => {
    const x = gridOffsetX + u.x * tileSize + tileSize / 2;
    const y = gridOffsetY + u.y * tileSize + tileSize / 2;
    ctx.fillStyle = u.color;
    ctx.beginPath();
    ctx.arc(x, y, tileSize / 2 - 8, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#fff';
    ctx.font = `${Math.floor(tileSize * 0.45)}px Arial`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(u.icon, x, y - 1);
  });
}

function updateProfile(unit) {
  profileIcon.textContent = unit.icon;
  profileName.textContent = unit.name.toUpperCase();
  profileHp.textContent = `${unit.hp} / ${unit.maxHp}`;
  profileMp.textContent = `${unit.mp} / ${unit.maxMp}`;
  profileRange.textContent = unit.range;
  profileLevel.textContent = unit.level;
}

function clearSelection() {
  selectedUnit = null;
  selectedAction = null;
  validMoves = [];
  validTargets = [];
  btnMove.disabled = true;
  btnAttack.disabled = true;
  btnFortify.disabled = true;
  draw();
}

function selectUnit(unit) {
  selectedUnit = unit;
  selectedAction = null;
  validMoves = [];
  validTargets = [];
  const active = unit.owner === 'player' && isPlayerTurn;
  btnMove.disabled = !active || unit.mp <= 0;
  btnAttack.disabled = !active;
  btnFortify.disabled = !active;
  updateProfile(unit);
  draw();
}

function executeMove(unit, x, y) {
  const dist = Math.abs(unit.x - x) + Math.abs(unit.y - y);
  if (dist > unit.mp) return;
  unit.x = x;
  unit.y = y;
  unit.mp -= dist;
  log(`${unit.name} átcsoportosítva a ${x},${y} mezőre.`);
  selectedAction = null;
  validMoves = [];
  selectUnit(unit);
}

function executeAttack(attacker, defender) {
  const { min, max } = parseRange(attacker.range);
  const dist = Math.abs(attacker.x - defender.x) + Math.abs(attacker.y - defender.y);
  if (dist < min || dist > max) return;

  const damage = Math.floor(Math.random() * 20) + 30;
  defender.hp = Math.max(0, defender.hp - damage);
  log(`${attacker.name} megtámadta ${defender.name} egységet. Sebzés: ${damage} HP.`);

  if (defender.hp <= 0) {
    units = units.filter(u => u.id !== defender.id);
    log(`${defender.name} megsemmisült.`);
  }

  attacker.mp = 0;
  selectedAction = null;
  validTargets = [];
  if (selectedUnit && units.includes(selectedUnit)) selectUnit(selectedUnit);
  else clearSelection();
}

function handleGridClick(x, y) {
  if (!isPlayerTurn) return;

  if (selectedAction === 'move') {
    const targetMove = validMoves.find(m => m.x === x && m.y === y);
    if (targetMove) return executeMove(selectedUnit, x, y);
  }

  if (selectedAction === 'attack') {
    const targetEnemy = validTargets.find(t => t.x === x && t.y === y);
    if (targetEnemy) return executeAttack(selectedUnit, targetEnemy);
  }

  const clickedUnit = units.find(u => u.x === x && u.y === y);
  if (clickedUnit && clickedUnit.owner === 'player') selectUnit(clickedUnit);
  else clearSelection();
}

function endTurn() {
  isPlayerTurn = false;
  selectedAction = null;
  validMoves = [];
  validTargets = [];
  log('ELLENSÉG KÖRE KÖVETKEZIK...');
  setTimeout(() => {
    units.filter(u => u.owner === 'enemy').forEach(enemy => {
      const target = units.find(u => u.owner === 'player');
      if (!target) return;
      const dist = Math.abs(enemy.x - target.x) + Math.abs(enemy.y - target.y);
      if (dist <= parseRange(enemy.range).max) {
        const damage = Math.floor(Math.random() * 15) + 20;
        target.hp = Math.max(0, target.hp - damage);
        log(`${enemy.name} támadta ${target.name} egységet. Sebzés: ${damage} HP.`);
        if (target.hp <= 0) units = units.filter(u => u.id !== target.id);
      }
    });

    units.forEach(u => u.mp = u.maxMp);
    isPlayerTurn = true;
    btnEndTurn.disabled = false;
    draw();
  }, 700);
}

function resetGame() {
  units = createUnits();
  isPlayerTurn = true;
  selectedUnit = null;
  selectedAction = null;
  validMoves = [];
  validTargets = [];
  profileIcon.textContent = '🤖';
  profileName.textContent = 'VÁLASSZ EGYSÉGET';
  profileHp.textContent = '-';
  profileMp.textContent = '-';
  profileRange.textContent = '-';
  profileLevel.textContent = '-';
  btnMove.disabled = true;
  btnAttack.disabled = true;
  btnFortify.disabled = true;
  btnEndTurn.disabled = false;
  draw();
}

btnMove.addEventListener('click', () => {
  if (!selectedUnit || selectedUnit.owner !== 'player' || selectedUnit.mp <= 0) return;
  selectedAction = 'move';
  validMoves = [];
  for (let r = 0; r < GRID_SIZE; r++) {
    for (let c = 0; c < GRID_SIZE; c++) {
      const dist = Math.abs(selectedUnit.x - c) + Math.abs(selectedUnit.y - r);
      if (dist > 0 && dist <= selectedUnit.mp && gameMap[r][c] !== 2 && gameMap[r][c] !== 3 && !units.some(u => u.x === c && u.y === r)) {
        validMoves.push({ x: c, y: r });
      }
    }
  }
  draw();
});

btnAttack.addEventListener('click', () => {
  if (!selectedUnit || selectedUnit.owner !== 'player') return;
  selectedAction = 'attack';
  validTargets = [];
  const { min, max } = parseRange(selectedUnit.range);
  units.forEach(u => {
    if (u.owner === 'enemy') {
      const dist = Math.abs(selectedUnit.x - u.x) + Math.abs(selectedUnit.y - u.y);
      if (dist >= min && dist <= max) validTargets.push(u);
    }
  });
  draw();
});

btnFortify.addEventListener('click', () => {
  if (!selectedUnit) return;
  selectedUnit.mp = 0;
  log(`${selectedUnit.name} sánc állásba került.`);
  selectUnit(selectedUnit);
});

btnEndTurn.addEventListener('click', endTurn);
btnRestart.addEventListener('click', resetGame);

canvas.addEventListener('click', e => {
  const rect = canvas.getBoundingClientRect();
  const x = Math.floor((e.clientX - rect.left - gridOffsetX) / tileSize);
  const y = Math.floor((e.clientY - rect.top - gridOffsetY) / tileSize);
  if (x >= 0 && x < GRID_SIZE && y >= 0 && y < GRID_SIZE) handleGridClick(x, y);
});

window.addEventListener('resize', resizeCanvas);
window.addEventListener('load', () => {
  resizeCanvas();
  units.forEach(u => u.mp = u.maxMp);
  btnEndTurn.disabled = false;
  draw();
});
