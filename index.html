<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aviator Crash Game</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        body { font-family: 'Inter', sans-serif; }
        .tab-content { display: none; }
        .tab-content.active { display: block; }
    </style>
</head>
<body class="bg-slate-100 text-slate-800 min-h-screen flex flex-col">

    <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-md mx-auto px-4 py-3 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <div class="w-8 h-8 bg-blue-500 rounded-full flex items-center justify-center text-white font-bold">
                    <i class="fa-solid fa-plane-departure text-sm"></i>
                </div>
                <div>
                    <h1 class="text-sm font-bold text-slate-700" id="user-name-display">Mironshoh</h1>
                    <p class="text-xs text-slate-400">ID: 874921</p>
                </div>
            </div>
            <div class="bg-slate-50 border border-slate-200 rounded-lg px-3 py-1.5 text-right">
                <span class="text-xs text-slate-500 block font-medium">Balans</span>
                <span class="text-sm font-bold text-blue-600" id="main-balance">0 UZS</span>
            </div>
        </div>
    </header>

    <main class="flex-1 max-w-md w-full mx-auto p-4 pb-24">
        
        <div id="tab-game" class="tab-content active space-y-4">
            <div class="bg-white p-2 rounded-xl border border-slate-200 shadow-sm flex gap-1.5 overflow-x-auto text-xs font-semibold" id="history-badges">
                <span class="bg-slate-100 text-slate-600 px-2 py-1 rounded">1.24x</span>
                <span class="bg-blue-50 text-blue-600 px-2 py-1 rounded">5.40x</span>
                <span class="bg-slate-100 text-slate-600 px-2 py-1 rounded">2.10x</span>
                <span class="bg-blue-100 text-blue-700 px-2 py-1 rounded">14.20x</span>
                <span class="bg-slate-100 text-slate-600 px-2 py-1 rounded">1.05x</span>
            </div>

            <div class="bg-slate-900 rounded-2xl h-52 relative overflow-hidden flex flex-col items-center justify-center border border-slate-800 shadow-inner">
                <div class="absolute inset-0 opacity-10 bg-[linear-gradient(to_right,#808080_1px,transparent_1px),linear-gradient(to_bottom,#808080_1px,transparent_1px)] bg-[size:24px_24px]"></div>
                
                <div class="z-10 text-center">
                    <span class="text-5xl font-black text-white tracking-tight" id="live-multiplier">1.00x</span>
                    <p class="text-xs text-slate-400 mt-1 hidden" id="game-status-text">Samolyot uchmoqda...</p>
                </div>

                <div class="absolute bottom-6 left-6 text-blue-400 text-3xl opacity-0 transition-all duration-100 ease-linear" id="plane-element">
                    <i class="fa-solid fa-plane"></i>
                </div>
            </div>

            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div class="flex gap-2">
                    <div class="relative flex-1">
                        <span class="absolute left-3 top-2.5 text-xs text-slate-400 font-bold">UZS</span>
                        <input type="number" id="bet-amount" value="10000" step="5000" min="1000" class="w-full bg-slate-50 border border-slate-200 rounded-xl pl-12 pr-3 py-2 text-sm font-bold focus:outline-none focus:border-blue-500">
                    </div>
                    <div class="flex gap-1 bg-slate-100 p-1 rounded-xl">
                        <button onclick="adjustBet(5000)" class="px-2.5 text-xs font-bold text-slate-600 hover:bg-white rounded-lg transition">+5k</button>
                        <button onclick="adjustBet(20000)" class="px-2.5 text-xs font-bold text-slate-600 hover:bg-white rounded-lg transition">+20k</button>
                    </div>
                </div>

                <button id="main-bet-btn" onclick="handleBetAction()" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-3.5 rounded-xl shadow-lg shadow-blue-500/20 transition-all text-center flex flex-col items-center justify-center">
                    <span class="text-base" id="btn-primary-text">TIKISH KIRITISH</span>
                    <span class="text-xs opacity-80 font-normal" id="btn-sub-text">Samolyot uchishidan oldin</span>
                </button>
            </div>
        </div>

        <div id="tab-history" class="tab-content space-y-4">
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
                <h3 class="text-sm font-bold text-slate-700 mb-3"><i class="fa-solid fa-clock-rotate-left text-blue-500 mr-2"></i>Tikishlar Tarixi</h3>
                <div class="divide-y divide-slate-100 max-h-60 overflow-y-auto" id="bets-history-list">
                    <div class="py-2.5 flex justify-between items-center text-sm">
                        <div>
                            <p class="font-semibold text-slate-700">10,000 UZS</p>
                            <p class="text-xs text-slate-400">Bugun, 14:21</p>
                        </div>
                        <span class="text-green-600 font-bold bg-green-50 px-2 py-0.5 rounded text-xs">+15,400 UZS (1.54x)</span>
                    </div>
                </div>
            </div>

            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
                <h3 class="text-sm font-bold text-slate-700 mb-3"><i class="fa-solid fa-wallet text-blue-500 mr-2"></i>Depozit Jurnali</h3>
                <div class="divide-y divide-slate-100" id="deposit-history-list">
                    <div class="py-2.5 flex justify-between items-center text-sm">
                        <div>
                            <p class="font-semibold text-slate-700">50,000 UZS</p>
                            <p class="text-xs text-slate-400">Kecha, 18:05</p>
                        </div>
                        <span class="text-blue-600 font-medium bg-blue-50 px-2 py-0.5 rounded text-xs">Muvaffaqiyatli</span>
                    </div>
                </div>
            </div>
        </div>

        <div id="tab-account" class="tab-content space-y-4">
            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div class="flex items-center gap-3">
                    <div class="w-12 h-12 bg-slate-100 rounded-full flex items-center justify-center text-slate-500 text-xl">
                        <i class="fa-solid fa-circle-user"></i>
                    </div>
                    <div>
                        <h4 class="font-bold text-slate-800" id="prof-name">Mironshoh</h4>
                        <p class="text-xs text-slate-400" id="prof-phone">+998 (99) 123-4567</p>
                    </div>
                </div>
                
                <div class="grid grid-cols-2 gap-2 pt-2">
                    <button onclick="openDepositModal()" class="bg-blue-500 hover:bg-blue-600 text-white text-xs font-bold py-2.5 px-4 rounded-xl transition flex items-center justify-center gap-1.5">
                        <i class="fa-solid fa-plus-circle"></i> Balans Qo'shish
                    </button>
                    <button onclick="handleWithdrawal()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold py-2.5 px-4 rounded-xl transition flex items-center justify-center gap-1.5">
                        <i class="fa-solid fa-money-bill-transfer"></i> Pul Yechish
                    </button>
                </div>
            </div>

            <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm space-y-3">
                <div class="flex justify-between items-start">
                    <div>
                        <h3 class="text-sm font-bold text-slate-700">Referal Tizimi</h3>
                        <p class="text-xs text-slate-400 mt-0.5">Har bir taklifga <span class="text-blue-600 font-bold" id="ref-bonus-text">10 000 UZS</span> oling</p>
                    </div>
                    <span class="bg-blue-50 text-blue-600 font-bold text-xs px-2 py-1 rounded-lg" id="ref-count">0 ta taklif</span>
                </div>
                <div class="flex gap-2">
                    <input type="text" readonly value="https://aviaplay.uz/ref?id=874921" class="bg-slate-50 border border-slate-200 rounded-xl px-3 py-2 text-xs font-medium text-slate-500 flex-1 focus:outline-none">
                    <button onclick="alert('Havola nusxalandi!')" class="bg-slate-800 hover:bg-slate-900 text-white text-xs font-bold px-4 rounded-xl transition">Nusxalash</button>
                </div>
            </div>
        </div>

    </main>

    <div id="deposit-modal" class="fixed inset-0 bg-slate-900/60 z-50 flex items-center justify-center p-4 hidden backdrop-blur-sm">
        <div class="bg-white w-full max-w-sm rounded-2xl p-5 space-y-4 shadow-xl">
            <div class="flex justify-between items-center border-b border-slate-100 pb-2">
                <h3 class="font-bold text-slate-800">Balansni To'ldirish</h3>
                <button onclick="closeDepositModal()" class="text-slate-400 hover:text-slate-600"><i class="fa-solid fa-xmark text-lg"></i></button>
            </div>
            
            <div class="bg-blue-50 border border-blue-100 rounded-xl p-3 text-center">
                <p class="text-xs text-blue-600 font-medium">To'lovni amalga oshirish uchun taymer:</p>
                <p class="text-2xl font-black text-blue-700 mt-0.5" id="deposit-timer">05:00</p>
            </div>

            <div class="space-y-2">
                <label class="text-xs text-slate-400 font-bold uppercase tracking-wider block">HUMO Karta Raqami</label>
                <div class="bg-slate-50 border border-slate-200 rounded-xl p-3 flex justify-between items-center">
                    <span class="font-mono font-bold text-slate-700 tracking-wider text-sm" id="card-number">9860 1201 4332 6722</span>
                    <button onclick="navigator.clipboard.writeText('9860120143326722'); alert('Karta raqami nusxalandi!');" class="text-blue-500 hover:text-blue-600 text-xs font-bold"><i class="fa-regular fa-copy"></i></button>
                </div>
            </div>

            <div class="text-xs text-slate-400 space-y-1">
                <p class="flex items-center gap-1.5"><i class="fa-solid fa-circle-info text-blue-500"></i> Kartaga pul o'tkazgach, tizim uni 5 daqiqa ichida avtomatik hisoblaydi.</p>
            </div>

            <button onclick="closeDepositModal()" class="w-full bg-slate-800 hover:bg-slate-900 text-white font-bold py-2.5 rounded-xl transition text-sm">Yopish</button>
        </div>
    </div>

    <nav class="bg-white border-t border-slate-200 fixed bottom-0 left-0 right-0 z-40 shadow-[0_-2px_10px_rgba(0,0,0,0.03)]">
        <div class="max-w-md mx-auto px-6 py-2 flex justify-between items-center">
            <button onclick="switchTab('game')" id="nav-game" class="flex flex-col items-center gap-1 text-blue-500 transition font-medium">
                <i class="fa-solid fa-gamepad text-lg"></i>
                <span class="text-[10px]">O'yinlar</span>
            </button>
            <button onclick="switchTab('history')" id="nav-history" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition font-medium">
                <i class="fa-solid fa-chart-line text-lg"></i>
                <span class="text-[10px]">Tarix</span>
            </button>
            <button onclick="switchTab('account')" id="nav-account" class="flex flex-col items-center gap-1 text-slate-400 hover:text-slate-600 transition font-medium">
                <i class="fa-solid fa-user text-lg"></i>
                <span class="text-[10px]">Akkaunt</span>
            </button>
        </div>
    </nav>

    <script>
        // App State
        let balance = 25000; // Boshlang'ich sinov balansi (UZS)
        let isPlaying = false;
        let isBetPlaced = false;
        let currentMultiplier = 1.00;
        let gameInterval = null;
        let currentBetAmount = 10000;
        let timerInterval = null;
        
        // Dynamic Loss Controls & Psychological Hook Configurations
        let betCount = 0; // Foydalanuvchining o'yinlar soni
        let crashPoint = 2.50; // Dynamic belgilangan nuqta

        // Initialize display
        updateBalanceDisplay();

        function updateBalanceDisplay() {
            document.getElementById('main-balance').innerText = balance.toLocaleString() + ' UZS';
        }

        // Tab Switching Logic
        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.getElementById('tab-' + tabId).classList.add('active');

            // Update nav indicators
            const tabs = ['game', 'history', 'account'];
            tabs.forEach(t => {
                const btn = document.getElementById('nav-' + t);
                if (t === tabId) {
                    btn.classList.remove('text-slate-400');
                    btn.classList.add('text-blue-500');
                } else {
                    btn.classList.remove('text-blue-500');
                    btn.classList.add('text-slate-400');
                }
            });
        }

        // Bet Amount Modifier Buttons
        function adjustBet(val) {
            if(isPlaying || isBetPlaced) return;
            currentBetAmount += val;
            if(currentBetAmount < 1000) currentBetAmount = 1000;
            document.getElementById('bet-amount').value = currentBetAmount;
        }

        // Game Simulation Loop
        function handleBetAction() {
            currentBetAmount = parseInt(document.getElementById('bet-amount').value) || 10000;

            if (!isBetPlaced && !isPlaying) {
                // Place Bet
                if (balance < currentBetAmount) {
                    alert("Mablag' yetarli emas! Iltimos, hisobni to'ldiring.");
                    return;
                }
                balance -= currentBetAmount;
                updateBalanceDisplay();
                isBetPlaced = true;
                
                // UI Changes to Awaiting Flight
                document.getElementById('main-bet-btn').classList.replace('bg-blue-500', 'bg-amber-500');
                document.getElementById('btn-primary-text').innerText = "PARVOZ KUTILMOQDA...";
                document.getElementById('btn-sub-text').innerText = "O'yin tez orada boshlanadi";
                
                // Trigger auto flight start simulation delay
                setTimeout(startFlight, 2000);
            } else if (isPlaying) {
                // Cashout Action
                isPlaying = false;
                let winAmount = Math.floor(currentBetAmount * currentMultiplier);
                balance += winAmount;
                updateBalanceDisplay();
                
                // Add to History logs
                addBetToHistory(currentBetAmount, currentMultiplier, winAmount, true);

                alert(`Yutuq! Siz ${winAmount.toLocaleString()} UZS yutib oldingiz! (${currentMultiplier.toFixed(2)}x)`);
                resetGameUI();
            }
        }

        function startFlight() {
            if(!isBetPlaced) return;
            isBetPlaced = false;
            isPlaying = true;
            currentMultiplier = 1.00;
            betCount++;

            // RTP control logic simulator implementation
            // 1. New User Psychological Hook (1-3 games: high multipliers 7x - 20x)
            if (betCount <= 2) {
                crashPoint = (Math.random() * (20.00 - 7.00) + 7.00);
            } else { 
                // 2. Dynamic Loss Algoritm Mode (Cap Max 30x, keep low frequently)
                let rand = Math.random();
                if (rand < 0.6) {
                    crashPoint = (Math.random() * (1.80 - 1.01) + 1.01); // 60% loss chance instantly
                } else {
                    crashPoint = (Math.random() * (29.99 - 2.00) + 2.00); // 40% chance up to 30x max
                }
            }

            // Change UI Button to Cashout state
            document.getElementById('main-bet-btn').classList.replace('bg-amber-500', 'bg-blue-600');
            document.getElementById('btn-primary-text').innerText = "CHIQARIB OLISH (CASH OUT)";
            document.getElementById('game-status-text').classList.remove('hidden');
            
            // Plane Visual Animation Start
            const plane = document.getElementById('plane-element');
            plane.style.opacity = '1';

            gameInterval = setInterval(() => {
                if (currentMultiplier >= crashPoint) {
                    // CRASHED!
                    clearInterval(gameInterval);
                    if (isPlaying) { 
                        // User didn't cash out in time
                        addBetToHistory(currentBetAmount, currentMultiplier, 0, false);
                        document.getElementById('live-multiplier').classList.replace('text-white', 'text-red-500');
                        document.getElementById('live-multiplier').innerText = "CRASHED";
                        isPlaying = false;
                    }
                    setTimeout(resetGameUI, 2500);
                    return;
                }

                // Smooth exponential growth feel
                let increment = currentMultiplier * 0.012 + 0.01;
                currentMultiplier += increment;
                document.getElementById('live-multiplier').innerText = currentMultiplier.toFixed(2) + 'x';
                document.getElementById('btn-sub-text').innerText = "Joriy yutuq: " + Math.floor(currentBetAmount * currentMultiplier).toLocaleString() + " UZS";
                
                // Move plane graphic slightly up and right
                let progress = (currentMultiplier / 30) * 100;
                plane.style.bottom = `${Math.min(6 + progress * 1.2, 75)}%`;
                plane.style.left = `${Math.min(6 + progress * 2.5, 80)}%`;

            }, 80);
        }

        function resetGameUI() {
            clearInterval(gameInterval);
            isPlaying = false;
            isBetPlaced = false;
            
            // Reset Badge History UI
            if (currentMultiplier > 1.01 && document.getElementById('live-multiplier').innerText !== "CRASHED") {
                const badgeBox = document.getElementById('history-badges');
                const badge = document.createElement('span');
                badge.className = currentMultiplier >= 7 ? "bg-blue-100 text-blue-700 px-2 py-1 rounded" : "bg-slate-100 text-slate-600 px-2 py-1 rounded";
                badge.innerText = currentMultiplier.toFixed(2) + 'x';
                badgeBox.insertBefore(badge, badgeBox.firstChild);
            }

            // UI Elements defaults
            document.getElementById('live-multiplier').className = "text-5xl font-black text-white tracking-tight";
            document.getElementById('live-multiplier').innerText = "1.00x";
            document.getElementById('game-status-text').classList.add('hidden');
            
            const btn = document.getElementById('main-bet-btn');
            btn.className = "w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-3.5 rounded-xl shadow-lg shadow-blue-500/20 transition-all text-center flex flex-col items-center justify-center";
            document.getElementById('btn-primary-text').innerText = "TIKISH KIRITISH";
            document.getElementById('btn-sub-text').innerText = "Samolyot uchishidan oldin";
            
            const plane = document.getElementById('plane-element');
            plane.style.opacity = '0';
            plane.style.bottom = '1.5rem';
            plane.style.left = '1.5rem';
        }

        function addBetToHistory(bet, mult, win, isWin) {
            const list = document.getElementById('bets-history-list');
            const row = document.createElement('div');
            row.className = "py-2.5 flex justify-between items-center text-sm";
            
            let statusBadge = isWin 
                ? `<span class="text-green-600 font-bold bg-green-50 px-2 py-0.5 rounded text-xs">+${win.toLocaleString()} UZS (${mult.toFixed(2)}x)</span>`
                : `<span class="text-red-500 font-medium bg-red-50 px-2 py-0.5 rounded text-xs">Yutqazildi (${mult.toFixed(2)}x)</span>`;

            row.innerHTML = `
                <div>
                    <p class="font-semibold text-slate-700">${bet.toLocaleString()} UZS</p>
                    <p class="text-xs text-slate-400">Hozirgina</p>
                </div>
                ${statusBadge}
            `;
            list.insertBefore(row, list.firstChild);
        }

        // Financial & Modals Logic
        function openDepositModal() {
            document.getElementById('deposit-modal').classList.remove('hidden');
            startDepositTimer(300); // 5 daqiqa (300 soniya)
        }

        function closeDepositModal() {
            document.getElementById('deposit-modal').classList.add('hidden');
            clearInterval(timerInterval);
        }

        function startDepositTimer(duration) {
            clearInterval(timerInterval);
            let timer = duration, minutes, seconds;
            const display = document.getElementById('deposit-timer');
            
            timerInterval = setInterval(() => {
                minutes = parseInt(timer / 60, 10);
                seconds = parseInt(timer % 60, 10);

                minutes = minutes < 10 ? "0" + minutes : minutes;
                seconds = seconds < 10 ? "0" + seconds : seconds;

                display.innerText = minutes + ":" + seconds;

                if (--timer < 0) {
                    clearInterval(timerInterval);
                    display.innerText = "Muddati tugadi";
                }
            }, 1000);
        }

        function handleWithdrawal() {
            const minWithdraw = 160000;
            if (balance < minWithdraw) {
                alert(`Minimal yechish summasi: ${minWithdraw.toLocaleString()} UZS. Sizning balansingiz yetarli emas!`);
            } else {
                alert("Yechish arizasi tasdiqlandi. Admin profiliga yo'naltirilmoqdasiz...");
                // Admin Telegram profiliga yo'naltirish
                window.location.href = "https://t.me/your_admin_username"; 
            }
        }
    </script>
</body>
</html>
