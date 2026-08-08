@echo off
chcp 65001 >nul 2>&1
cls
echo ============================================================
echo   Wison Doc Generators
echo ============================================================
echo.
echo   [1] gen_deficiency_report        -- CCECC Deficiency Rpt
echo   [2] gen_letter_0008              -- CCECC Final Cure Notice
echo   [3] gen_final_contract           -- METS Lab Contract
echo   [4] gen_seal_contract            -- LONGTAIDI Seal (Contract)
echo   [5] gen_loa_longtaidi            -- LONGTAIDI LOA
echo   [6] gen_seal_loa                 -- LONGTAIDI Seal (LOA)
echo   [7] gen_po_night_shift           -- Med Svc Night Shift PO
echo   [8] gen_service_instruction      -- Med Svc Instruction
echo   [9] gen_subcontractor_matrix     -- Subcontractor Matrix
echo.
echo   [0] Exit
echo.
set /p choice="Number: "
if "%choice%"=="1" call "D:\Wison\_tools\launchers\_RUN_gen_deficiency_report.bat" && goto end
if "%choice%"=="2" call "D:\Wison\_tools\launchers\_RUN_gen_letter_0008.bat" && goto end
if "%choice%"=="3" call "D:\Wison\_tools\launchers\_RUN_gen_final_contract.bat" && goto end
if "%choice%"=="4" call "D:\Wison\_tools\launchers\_RUN_gen_seal_instruction.bat" && goto end
if "%choice%"=="5" call "D:\Wison\_tools\launchers\_RUN_gen_loa_longtaidi.bat" && goto end
if "%choice%"=="6" call "D:\Wison\_tools\launchers\_RUN_gen_seal_instruction_loa.bat" && goto end
if "%choice%"=="7" call "D:\Wison\_tools\launchers\_RUN_gen_po_night_shift.bat" && goto end
if "%choice%"=="8" call "D:\Wison\_tools\launchers\_RUN_gen_service_instruction.bat" && goto end
if "%choice%"=="9" call "D:\Wison\_tools\launchers\_RUN_gen_subcontractor_matrix.bat" && goto end
if "%choice%"=="0" goto end
echo Invalid.
pause
:end
